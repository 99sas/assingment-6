
class Counter:
    count = 0

    def __init__(self):
      Counter.count += 1

      @classmethod
      def show__count(cls):
         print(f"Total object created: {cls.count}")

cl = Counter()
c2 = Counter()
Counter.show_count()