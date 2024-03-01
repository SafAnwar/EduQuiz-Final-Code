class AnswerComparison:
  def __init__(self, user_answer, actual_answer):
      if not isinstance(user_answer, str) or not isinstance(actual_answer, str):
          raise TypeError("Both user_answer and actual_answer must be strings")

      if not user_answer or not actual_answer:
          raise ValueError("Both user_answer and actual_answer must not be empty")

      self.user_answer = user_answer.lower().split()
      self.actual_answer = actual_answer.lower().split()
      self.percentage_match = AnswerComparison.calculate_percentage_match(self)

  def calculate_similarity(self):
      if not self.user_answer or not self.actual_answer:
          return 0.0  # Return 0 if either of the answers is empty

      user_answer_set = set(self.user_answer)
      actual_answer_set = set(self.actual_answer)
      intersection = len(user_answer_set.intersection(actual_answer_set))
      union = len(user_answer_set.union(actual_answer_set))
      similarity = intersection / union if union != 0 else 0.0
      return similarity

  def calculate_percentage_match(self):
      similarity = self.calculate_similarity()
      percentage_match = similarity * 100
      return percentage_match
