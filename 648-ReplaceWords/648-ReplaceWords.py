# Last updated: 9/27/2025, 11:36:40 PM
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        word_List = sentence.split(" ")  
        Sorted_dict = sorted(dictionary, key=len)  

        for root in Sorted_dict:
            count = len(root)
            for i, word in enumerate(word_List):
                count1 = len(word)
                if count1 >= count:  
                    if word[:count] == root:  
                        word_List[i] = root 

        return " ".join(word_List) 