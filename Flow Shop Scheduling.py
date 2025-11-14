from functools import lru_cache

# Flow Shop Scheduling using DP (Exact for small n)
# times[i] = (time_on_machine1, time_on_machine2)

def flowshop_dp(times):
    n = len(times)

    # Precompute completion times of each job alone
    # completion[j] = (end_time_M1, end_time_M2)
    completion = [(t[0], t[0] + t[1]) for t in times]

    @lru_cache(None)
    def solve(mask, last_m1, last_m2):
        # mask = subset of completed jobs
        # last_m1 = time when machine 1 is free
        # last_m2 = time when machine 2 is free

        if mask == (1 << n) - 1:
            return 0  # no extra makespan

        best = float('inf')

        for job in range(n):
            if not (mask & (1 << job)):
                t1, t2 = times[job]

                # Machine 1 finishes this job at:
                finish_m1 = last_m1 + t1

                # Machine 2 can start only after BOTH:
                # 1) Machine 2 is free
                # 2) Machine 1 completed the job
                start_m2 = max(finish_m1, last_m2)
                finish_m2 = start_m2 + t2

                # DP on the updated future
                result = finish_m2 + solve(mask | (1 << job),
                                           finish_m1,
                                           finish_m2)

                best = min(best, result)

        return best

    # start with no jobs completed, both machines idle at time 0
    return solve(0, 0, 0)



# Example with 3 jobs (Machine1, Machine2 times)
jobs = [
    (2, 3),
    (1, 4),
    (3, 2)
]

print("Minimum Makespan:", flowshop_dp(jobs))