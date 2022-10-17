class DreamTeamApi extends Api {

	constructor(method="GET", id="0", payload={}) {
		let url = `http://localhost:8000/dreamTeam`
        if(method == "DELETE") {
		    url = `http://localhost:8000/dreamTeam/${id}`
        }
		super(new AjaxCall(method, payload), url)
	}

	async getData() {
        console.log("getting dream team - metadata call");
		return await this.callApi()
	}

    async addPlayer() {
		return await this.callApi()
    }

 
}