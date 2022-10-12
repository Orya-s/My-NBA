/* Renderer Module
Renderer is a class which should render each section of the user page through Handlebars (and jQuery). 
*/


const nbaRender = function() {

    function renderPlayers(players) {
        // console.log(players);
        $(".cards-container").empty();

        const source = $('#cards-template').html();
        const template = Handlebars.compile(source);
        const newHTML = template(players); 
        $('.cards-container').append(newHTML);
    }

    function renderPictures() {

    }


    return {
        renderPlayers,
        renderPictures
    }
}