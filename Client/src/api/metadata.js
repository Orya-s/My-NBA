class MetaDataApi extends Api {

	constructor(year = "2018", team = "lakers", active = "", apiInterface = new AjaxCall()) {
		let url = `http://localhost:8000/search?teamName=${team}&year=${year}&active=${active}`
		super(apiInterface, url)
	}

	async getData() {
        console.log("performing metadata call");
		return await this.callApi()
	}
}