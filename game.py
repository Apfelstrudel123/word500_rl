from data_loader import sampleWord

MAX_ATTEMPTS = 8

class Game:
    def __init__(self, data):
        self.words = data
        self.solution = sampleWord(data)
        self.word_len = len(self.solution)
        self.attempts = 0
        self.finished = False
        print(self.solution)

    def getRemainingAttempts(self):
        return MAX_ATTEMPTS - self.attempts

    def evalWord(self, word):
        if len(word) != self.word_len:
            print("Error: Word length mismatch.")
            return False, 0, 0, 0
        if self.finished:
            print("Error: Word evaluated after game has ended.")
            return False, 0, 0, 0

        word = word.lower()
        if word not in self.words:
            print("Error: Word unknown.")
            return False, 0, 0, 0
        
        self.attempts += 1
        if self.attempts == MAX_ATTEMPTS:
            self.finished = True

        num_red = 0
        num_yellow = 0
        num_green = 0

        solution_matched = [False] * len(self.solution)
        word_matched = [False] * len(word)

        for i in range(self.word_len):
            if word[i] == self.solution[i]:
                num_green += 1
                solution_matched[i] = True
                word_matched[i] = True

        for i in range(len(word)):
            if word_matched[i]:
                continue
    
            char = word[i]
            found_yellow = False
    
            for j in range(len(self.solution)):
                if not solution_matched[j] and self.solution[j] == char:
                    solution_matched[j] = True
                    found_yellow = True
                    break
            
            if found_yellow:
                num_yellow += 1
            else:
                num_red += 1

        #index = 0
        #for char in word:
        #    if char not in self.solution:
        #        num_red += 1
        #    elif char == self.solution[index]:
        #        if index in chars_used:
        #            num_yellow -= 1
        #        else:
        #            chars_used.append(index)
        #        num_green += 1
        #    else:
        #        num_yellow += 1
        #        chars_used.append(index)
        #    index += 1

        if num_green == self.word_len:
            print("Game solved! Solution was: ", self.solution)
            self.finished = True
        elif self.finished:
            print("Game lost! Solution was: ", self.solution)

        return True, num_red, num_yellow, num_green
        