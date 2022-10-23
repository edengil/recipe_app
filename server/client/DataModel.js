class Recipe {
    constructor() {
        this.idMeal = "";
        this.title = "";
        this.strCategory = "";
        this.strInstructions = "";
        this.thumbnail = "";
        this.href = "";
        this.ingredients = "";
        this.hasGluten = "";
        this.hasDairy = "";
    }
}



class Recipes {
    constructor() {
        this.all_recipes = [];
    }
    async fetchRecipes(ingredient, fillterGluten, fillterDairy) {
        const respons = await $.get(`/recipes?ingredient=${ingredient}&fillterGluten=${fillterGluten}&fillterDairy=${fillterDairy}`)
        // console.log(respons);
        for (const p of respons) {
            // console.log(p);
            // console.log(p);
            // console.log(p);
            let recipe = new Recipe()
            recipe.idMeal = p["idMeal"];
            recipe.title = p["title"];
            recipe.strCategory = p["strCategory"];
            recipe.strInstructions = p["strInstructions"];
            recipe.thumbnail = p["thumbnail"];
            recipe.href = p["href"];
            recipe.ingredients = p["ingredients"];
            recipe.hasGluten = p["hasGluten"];
            recipe.hasDairy = p["hasDairy"];
            this.all_recipes.push(recipe);
        }
        
    };
}

function creatAll(ingredient, fillterGluten, fillterDairy) {
    return __awaiter(this, void 0, void 0, function* () {
        all_recipes = new Recipes();
        yield all_recipes.fetchRecipes(ingredient, fillterGluten, fillterDairy).then((x) => { });
        return all_recipes;
    });
}

