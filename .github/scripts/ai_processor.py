#!/usr/bin/env python3
"""
AI Content Processing Script for GitHub Actions
Processes files using GitHub Models API with customizable prompts
"""

import os
import json
import requests
from pathlib import Path

def load_config():
    """Load configuration from config.json"""
    config_path = Path(__file__).parent / 'config.json'
    with open(config_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def get_changed_files():
    """Get list of changed files from environment"""
    files_str = os.environ.get('CHANGED_FILES', '')
    if not files_str:
        return []
    return [f.strip() for f in files_str.split('\n') if f.strip()]

def generate_output_filename(input_file):
    """Generate output filename with fixed suffix"""
    path_obj = Path(input_file)
    return path_obj.parent / f"{path_obj.stem}_processed.md"

def process_content(content, config, title=""):
    """Process content using GitHub Models API"""
    github_token = os.environ.get('GITHUB_TOKEN')
    if not github_token:
        raise ValueError("GITHUB_TOKEN environment variable not set")
    
    api_url = "https://models.github.ai/inference/chat/completions"
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {github_token}"
    }
    
    # Customize user message based on title
    user_content = content
    if title:
        user_content = f"Title: {title}\n\nContent:\n{content}"
    
    payload = {
        "model": config.get('model', 'gpt-4o-mini'),
        "messages": [
            {
                "role": "system",
                "content": config.get('system_prompt', 'You are a helpful assistant.')
            },
            {
                "role": "user",
                "content": user_content
            }
        ],
        "max_tokens": config.get('max_tokens', 1000),
        "temperature": config.get('temperature', 0.3)
    }
    
    try:
        response = requests.post(api_url, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
        
        result = response.json()
        return result['choices'][0]['message']['content']
        
    except requests.exceptions.RequestException as e:
        print(f"API request failed: {e}")
        if hasattr(e, 'response') and e.response:
            print(f"Response content: {e.response.text}")
        raise
    except (KeyError, IndexError) as e:
        print(f"Failed to parse API response: {e}")
        print(f"Response: {response.text}")
        raise

def main():
    """Main function to process files"""
    print("Starting AI content processing...")
    
    # Load configuration
    config = load_config()
    
    # Get changed files
    changed_files = get_changed_files()
    if not changed_files:
        print("No changed files found")
        return
    
    print(f"Found {len(changed_files)} changed files")
    
    processed_files = []
    
    for file_path in changed_files:
        print(f"\nProcessing: {file_path}")
        
        # Skip if not a markdown file
        if not file_path.endswith('.md'):
            print(f"Skipping non-markdown file: {file_path}")
            continue
        
        # Skip if it's already a processed file
        if file_path.endswith('_processed.md'):
            print(f"Skipping processed file: {file_path}")
            continue
        
        # Check if file exists
        if not os.path.exists(file_path):
            print(f"File not found: {file_path}")
            continue
        
        # Generate output file path
        output_file = generate_output_filename(file_path)
        
        # Skip if output already exists
        if output_file.exists():
            print(f"Output file already exists: {output_file}")
            continue
        
        try:
            # Read file content
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            path_obj = Path(file_path)
            title = path_obj.stem
            
            print(f"Processing content for: {title}")
            
            # Process content
            processed_content = process_content(content, config, title)
            
            # Write output file
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(f"# {title} - AI Processed\n\n")
                f.write(processed_content)
            
            print(f"Created processed file: {output_file}")
            processed_files.append(str(output_file))
            
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            continue
    
    # Output processed files for GitHub Actions
    if processed_files:
        print(f"\nProcessed {len(processed_files)} files:")
        for f in processed_files:
            print(f"  - {f}")
        
        # Set environment variable for git commit step
        with open(os.environ['GITHUB_OUTPUT'], 'a') as f:
            f.write(f"processed_files={','.join(processed_files)}\n")
    else:
        print("\nNo files processed")

if __name__ == "__main__":
    main()