class Solution:
    def findAllRecipes(self, recipes, ingredients, supplies):
        res = {}
        result = []
        for i in range(len(recipes)):
            res[recipes[i]] = ingredients[i]

        for key, val in res.items():
            if set(val).issubset(supplies):
                result.append(key)

        supplies += result

        for key, val in res.items():
            if set(val).issubset(supplies):
                result.append(key)

        return set(result)


s = Solution()
recipes = ["bread", "sandwich", "burger"]
ingredients = [["yeast", "flour"], ["bread", "meat"], ["sandwich", "meat", "bread"]]
supplies = ["yeast", "flour", "meat"]
print(s.findAllRecipes(recipes, ingredients, supplies))
