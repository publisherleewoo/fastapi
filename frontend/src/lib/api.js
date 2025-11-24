const fastapi = (operation, url, params, success_callback, failure_callback) => {
 

    let method = operation
    let content_type = 'application/json'
    let body = JSON.stringify(params)

    let _url = import.meta.env.VITE_SERVER_URL + url

    if (method === 'get') {
        _url += '?' + new URLSearchParams(params)
    }

    let opstions = {
        method: method,
        headers: {
            'Countent-Type': content_type
        }
    }

    if (method !== 'get') {
        opstions['body'] = body
    }

    fetch(_url, opstions)
        .then((response) => {
            response.json()
                .then(json => {
                    if (response.status >= 200 && response.status < 300) {
                        if (success_callback) {
                            success_callback(json)
                        }
                    } else {
                        if (failure_callback) {
                            failure_callback(json)
                        } else {
                            alert(JSON.stringify(json))
                        }
                    }
                }).catch(error => {
                    console.log('2에러 :', error)
                    alert(JSON.stringify(error))
                })
        })

}

export default fastapi