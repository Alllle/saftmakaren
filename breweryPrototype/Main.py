import MainView
import RecipeModels as rm

currentUser = rm.User(name = 'kurt')

if __name__ == "__main__":
    mainView = MainView.MainView()
    mainView.startApplication()

def addRecipe(args):
    new_recipe = rm.Recipe(title = args[0])
    currentUser.addRecipe(new_recipe)
    return args[0]
