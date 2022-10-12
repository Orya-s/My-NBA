class MetaDataApi extends Api {

	constructor(year = "2018", team = "lakers", apiInterface = new AjaxCall()) {
		let url = `http://localhost:8000/search?teamName=${team}&year=${year}`
		super(apiInterface, url)
	}

	async getData() {
        console.log("performing metadata call");
		return await this.callApi()
	}
}