/* Data Model
This model is in charge of handling all data related functionalities, it should make all the API's request 
and able to generate a user’s data.  */


const nbaData = function() {
    
    let players; 

    function init(year, team, active) {
        players = new MetaDataApi(year, team, active)
    }

    async function getData() {
        let nbaPromise = players.getData() 
        return await Promise.all([nbaPromise]).then(function(res) {
            players = res[0]
            return {players: res[0]}
        }) 
    }

    function getPlayerById(playerId) {
        let player; 
        for (const p of players) {
            if(p.id == playerId) {
                player = p;
            }
        }
        return player
    }

    async function addToDreamTeam(playerId) {
        let player = getPlayerById(playerId)
        player.dreamTeam = true
        let dreamTeamPlayers = new DreamTeamApi("POST", 0, player)
        await dreamTeamPlayers.callApi() 
    }

    async function removeFromDreamTeam(playerId) {
        let dreamTeamPlayers = new DreamTeamApi("DELETE", playerId)
        await dreamTeamPlayers.callApi()
    }

    async function getDreamTeam() {
        let dreamTeamPlayers = new DreamTeamApi()
        let dreamPromise = dreamTeamPlayers.callApi() 
        return await Promise.all([dreamPromise]).then(function(res) {
            return {players: res[0]}
        })  
    }

    return {
        init,
        getData,
        addToDreamTeam,
        getPlayerById,
        removeFromDreamTeam,
        getDreamTeam
    }
}
