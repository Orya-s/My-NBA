/* Data Model
This model is in charge of handling all data related functionalities, it should make all the API's request 
and able to generate a user’s data.  */


const nbaData = function() {
    
    let players; 

    function init(year, team) {
        players = new MetaDataApi(year, team)
    }

    async function getData() {
        let nbaPromise = players.getData() 
        return await Promise.all([nbaPromise]).then(function(res) {
            console.log(res[0]);    ///////////
            return {metaData: res[0]}
        }) 
    }

    return {
        init,
        getData
    }
}
