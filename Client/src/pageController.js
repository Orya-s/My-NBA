/* Controller
Guidelines for the controller:
Use the instances of your classes with MVC principles so that when the user clicks the generate user button, 
it will fetch and load the data on the screen  */

const nbaPlayers = nbaData()
const rendPage = nbaRender()
let inDream = false

$("#getTeamBtn").on("click", function() {
    inDream = false
    const year = $("#yearInput").val()
    const team = $("#teamInput").val()
    const active = $('#checkbox').val()
    
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
    const id = $(this).parent().prev().attr("id")

    if($(this).attr("dreamTeam") == "false") {
        nbaPlayers.addToDreamTeam(id)
        $(this).attr("dreamTeam", "true") 
        $(this).removeClass('add-dream');
        $(this).addClass('remove-dream');
        $(this).text("Remove from Dream Team")
    }
    else {
        nbaPlayers.removeFromDreamTeam(id)
        $(this).attr("dreamTeam", "false") 
        $(this).removeClass('remove-dream');
        $(this).addClass('add-dream');
        $(this).text("Add to Dream Team")

        if (inDream) {
            nbaPlayers.getDreamTeam().then((res) => {
                cleanInput()
                rendPage.rendDream(res)
                return res
            })
        }
    }
})


$("#DreamTeamBtn").on("click", function() {
    inDream = true
    nbaPlayers.getDreamTeam().then((res) => {
        cleanInput()
        rendPage.rendDream(res)
        return res
    })
})


$("body").on("click", ".fa", function() {
    $(this).siblings(".modal").css("display", "block");
    const fullName = $(this).parent().siblings(".fullName").text().trim().split(/\s+/);
    $(".stats-container").empty();
    nbaPlayers.getStats(fullName[1], fullName[0]).then((res) => { 
        rendPage.rendStats(res)
        return res
    })
})
// close stats
$("body").on("click", ".close", function() {
    $(this).closest(".modal").css("display", "none");
})
