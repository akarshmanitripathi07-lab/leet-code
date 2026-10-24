class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        def get_day_of_year(date: str) -> int:
            month = int(date[:2])
            day = int(date[3:])
            return sum(days_in_month[:month - 1]) + day
        
        startAlice = get_day_of_year(arriveAlice)
        endAlice = get_day_of_year(leaveAlice)
        startBob = get_day_of_year(arriveBob)
        endBob = get_day_of_year(leaveBob)
        
        overlap_start = max(startAlice, startBob)
        overlap_end = min(endAlice, endBob)
        
        return max(0, overlap_end - overlap_start + 1)