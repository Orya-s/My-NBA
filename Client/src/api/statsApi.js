class StatsApi extends Api {

	constructor(lname = "Booker", fname = "Devin", apiInterface = new AjaxCall()) {
		let url = `http://localhost:8000/stats/${lname}/${fname}`
		super(apiInterface, url)
	}

	async getData() {
		return await this.callApi()
	}
}