const api = {
    get: async function(url) {
        response = await fetch(url)
        return response.json()
    },
    post: async function(url, data) {
        response = await fetch(url, {
            method: "POST",
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        })
        return response
    },
    delete: async function(url) {
        response = await fetch(url, {method: "DELETE"})
        return response
    },
    companies: {
        _base_url: "/api/company/",
        list: function(){
            return api.get(this._base_url)
        },
        create: function(data) {
            return api.post(this._base_url, data)
        },
        delete: function(id) {
            return api.delete(`${this._base_url}${id}/`)
        },
    }
}
