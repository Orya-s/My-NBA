class AjaxCall {
	constructor(method="GET", payload={}) {
		this.method = method;
		this.payload = payload;
	}

	async getApi(url) {
		return await $.ajax({
			method: this.method,
			url: url,
			success: (result) => result,
			error: (result) => "error",
			dataType: "json",
			data: JSON.stringify(this.payload),
			contentType: "application/json"
		})
	}
}