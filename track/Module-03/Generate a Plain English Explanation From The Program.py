class Manager:
    def generate_explanation(self, match_count, required_count, missing_count):
        if required_count == 0:
            score_str = "0%"
        else:
            score = (match_count / required_count) * 100.0
            score_str = f"{score:.1f}%"
            
        return f"The student matches {match_count} out of {required_count} required skills. Match Score: {score_str}. Missing skills: {missing_count}."

match_count = int(input())
required_count = int(input())
missing_count = int(input())

manager = Manager()
print(manager.generate_explanation(match_count, required_count, missing_count))