/* Controller
Guidelines for the controller:
Use the instances of your classes with MVC principles so that when the user clicks the generate user button, 
it will fetch and load the data on the screen  */

const nbaPlayers = nbaData()
const rendPage = nbaRender()

$("#getTeamBtn").on("click", function() {
    const year = $("#yearInput").val()
    const team = $("#teamInput").val()
    const active = $('#checkbox').val()
    console.log(team + " " + year);     //////////
    
    if (team == "") {
        console.warn("team name is missing from input")
        alert("Please enter a team name!")
    }
    else {
        nbaPlayers.init(year, team, active);
        nbaPlayers.getData().then((res) => {
            cleanInput()
            rendPage.rendCards(res)
            rendPage.headline(year, team)
            return res
        })
    }
})

const cleanInput = function() {
    $("#yearInput").val("")
    $("#teamInput").val("")
}


$("#checkbox").on('change', function() {
    if ($(this).is(':checked')) {
      $(this).attr('value', 'true');
    } 
    else {
      $(this).attr('value', 'false');
    }
});


$("body").on("click", ".dream-btn", function() {
    $(this).toggleClass('add-dream');
    $(this).toggleClass('remove-dream');
    $(this).text($(this).text() == "Add to Dream Team" ? "Remove from Dream Team": "Add to Dream Team");
})

