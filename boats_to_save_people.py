class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i, j, no_of_boats = 0, len(people)-1, 0
        while i <= j:
            if i == j:
                no_of_boats += 1
                break
            total_weight = people[i] + people[j]
            if total_weight > limit:
                no_of_boats += 1
                j -= 1
            else:
                no_of_boats += 1
                i+=1
                j-=1
        return no_of_boats