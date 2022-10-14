/* Renderer Module
Renderer is a class which should render each section of the user page through Handlebars (and jQuery). 
*/


const nbaRender = function() {

    function renderPlayers(players) {
        $(".cards-container").empty();
        $(".title-container").empty();

        const source = $('#cards-template').html();
        const template = Handlebars.compile(source);
        const newHTML = template(players); 
        $('.cards-container').append(newHTML);
    }

    function renderPictures(metaData) {
        for (const player of metaData) {
			let elementToRender = `#${player.id}`
            let newHTML = `<img src=${player.img} onerror="this.src='https://www.edigitalagency.com.au/wp-content/uploads/NBA-logo-png.png';" alt="not found" />`
			
            $(elementToRender).empty()
			$(elementToRender).append(newHTML)
		}
    }

    function headline(year, team) {
        $(".title-container").prepend(`<div> Showing results for team <b>${team}</b> - <b>${year}</b> </div> <br>`)
    }

    function rendCards(res) {
        renderPlayers(res)  
        renderPictures(res.players)
    }

    return {
        headline,
        rendCards
    }
}