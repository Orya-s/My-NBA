/* Controller
Guidelines for the controller:
Use the instances of your classes with MVC principles so that when the user clicks the generate user button, 
it will fetch and load the data on the screen  */

const nbaPlayers = nbaData()
const rendPage = nbaRender()

$("#getTeamBtn").on("click", function() {
    const year = $("#yearInput").val()
    const team = $("#teamInput").val()
    console.log(team + " " + year);     //////////
    
    if (team == "") {
        console.warn("team name is missing from input")
        alert("Please enter a team name!")
    }
    else {
        nbaPlayers.init(year, team);
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