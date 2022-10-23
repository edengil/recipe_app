"use strict";
const Renderer = function (init) {
    const recipes = init;
    $(".quote-container").empty();
    const renderKanye = function () {
        $(".quote-container").empty();

        const source = $("#kanye-template").html();
        const template = Handlebars.compile(source);
        const newHTML = template(recipes);
        $(".quote-container").append(newHTML);
    };
    renderKanye();
};