
let recipes = new Recipes()

$(".generate-user").on("click",  function () {
  let ingredient = $(".ingredient").val();
  const fillterGluten = $(".accept_gluten").is(":checked");
  const fillterDairy = $(".accept_dairy").is(":checked");
  if (ingredient !== ""){
     recipes.fetchRecipes(ingredient,fillterGluten,fillterDairy).then(() => {
    let init = recipes.all_recipes
    //todo
    console.log(init);
    Renderer(init);
    }
)}
});
$(".quote-container").on("click", ".recipe-img", function () {
  const firstIngredient = $(this).closest(".card").find("li:first").html();
  alert(firstIngredient);
});