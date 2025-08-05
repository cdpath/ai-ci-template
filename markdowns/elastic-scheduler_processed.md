# elastic-scheduler - AI Processed

### Summary of Elastic Scheduler Feature in Volcano

#### Introduction
The Elastic Scheduler feature in Volcano enhances workload scheduling by optimizing resource utilization and reducing training job execution times. It allows for dynamic scheduling of training jobs (tfjob/pytorchjob/vcjob) within a Kubernetes cluster, utilizing a defined `[min,max]` configuration.

#### Example Scenario
- **Cluster Resources**: 10 GPUs
- **Job Queues**: Two queues (queue1 and queue2) with equal weights and non-reclaimable resources.
  
| Queue   | Weight | Reclaimable | Deserved GPUs |
|---------|--------|-------------|----------------|
| queue1  | 1      | false       | 5              |
| queue2  | 1      | false       | 5              |

#### Elastic Pods
- Elastic pods (pod6 to pod10) are designated as low-priority resources that can be preempted when resources are scarce.
- **Key Characteristics**:
  1. Created only when free resources are available.
  2. Preempted if there aren't enough resources for `minAvailable` pods.

#### Scheduling Principles
1. **Simultaneous Job Submission**: When jobs are submitted at the same time, `minAvailable` pods are prioritized over elastic pods.
2. **Preemption on Same Queue**: If a new job is submitted in the same queue, the elastic pods of the existing job are preempted.
3. **Cross-Queue Preemption**: Submitting a job in a different queue can also lead to preemption of elastic pods from the first job.

#### Design Components
1. **Enqueue Action**:
   - Adjusts job enqueue logic to allow for preemption of elastic pods.
   - Ensures that if total elastic resources cannot satisfy a new job's `minRequest`, the job remains pending.

2. **Allocate Action** (Already Implemented):
   - Initially creates all pods, scheduling `minAvailable` pods first, followed by elastic pods if resources permit.

3. **Preempt Action** (Already Implemented):
   - Preempts elastic pods within the same queue if there are starving jobs.
   - No preemption if total elastic resources cannot meet the starving job's `minRequest`.

4. **Reclaim Action**:
   - Reclaims elastic resources from a queue if it is overused, regardless of the queue's `reclaimable` status.

This structured approach to scheduling with elastic pods aims to maximize resource efficiency and ensure effective job execution in Kubernetes environments.