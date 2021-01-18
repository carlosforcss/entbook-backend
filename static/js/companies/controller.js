const form_data = {
    name: null,
    description: null,
    symbol: null,
    market_values: [],
}

function getCompanyFormData() {
    const name = document.getElementById("name").value
    const description = document.getElementById("description").value
    const symbol = document.getElementById("symbol").value
    // Reset form
    document.getElementById("name").value = ""
    document.getElementById("description").value = ""
    document.getElementById("symbol").value = ""
    document.getElementById("market-values-container").innerHTML = ""
    data = {
        name: name,
        description: description,
        symbol: symbol,

    }
    data.market_values = ""
    form_data.market_values.forEach(market_value => {
        data.market_values += `${market_value},`
    })
    form_data.market_values = []
    return data
} // end function

function generateDOMElement({tag, classes, attrs, content}){
    const element = document.createElement(tag)
    if(classes){
        classes.forEach((class_name) => element.classList.add(class_name))
    }
    if(attrs) {
        attrs.forEach(attr => {
            element.setAttribute(attr.name, attr.value)
        })
    }
    if(content){
        element.innerHTML = content
    }
    return element
} // end function

function generateEmptyCard(){
    const card = generateDOMElement({
        tag: "div",
        classes: ["card", "blue-grey", "darken-1"],
        content: `
            <div class="card-content white-text">
                <span class="card-title"></span>
                <p class="card-description"></p>
                <div class="market-values-container"></div>
                </div>
                <div class="card-action">
                    <button class="card-button btn edit-button">Edit</button>
                    <button class="card-button btn delete-button">Delete</button>
                </div>
            </div>
        `
    })
    return card
} // end function

function generateMarketValueTagElement(value){
    const new_value_element = generateDOMElement({
        tag: "div",
        classes: ['market-value-tag'],
        content: value,
    })
    const icon = generateDOMElement({
        tag: "i",
        classes: ["material-icons"],
        content: "remove_circle",
    })
    new_value_element.appendChild(icon)
    return new_value_element
} // end function

function addMarketValueToForm(value) {
    const container = document.getElementById("market-values-container")
    const value_element = generateMarketValueTagElement(value)
    value_element.addEventListener("click", (e) => {
        value_element.classList.add("d-none")
        form_data.market_values = form_data.market_values.filter(market_value => market_value != value)
    })
    container.appendChild(value_element)
} // end function

function handleCreateMarketValue(e) {
    if(e.key == ",") {
        const new_market_input = document.getElementById("market-value")
        const new_market_value = new_market_input.value.replace(",", "")
        if(new_market_value){
            new_market_input.value = ""
            form_data.market_values.push(new_market_value)
            addMarketValueToForm(new_market_value)
        }
    }
} // end functino

function showErrorModal(errors) {
    for(error_key in errors) {
        const error_list = errors[error_key]
        error_list.forEach(error => {
            const error_element = document.getElementById(`${error_key}-error`).innerHTML = error
        })
    }
} // end function

function handleCreateCompany(e) {
    data = getCompanyFormData()
    api.companies.create(data).then(response => {
        if(response.id){
            api.companies.list().then(response_list => {
                generateCompaniesList(response_list)
            })
        }else {
            showErrorModal(response)
        }
    })
} // end function

function generateCompaniesList(companies) {
    const companies_container = document.getElementById("companies-container")
    companies_container.innerHTML = ""
    companies.forEach((company) => {
        const card = generateEmptyCard()
        card.querySelector(".card-title").innerHTML = company.name
        card.querySelector(".card-description").innerHTML = company.description
        const card_container = generateDOMElement({
            tag: "div",
            classes: ["col", "s12", "m4"],
        })
        card_container.appendChild(card)
        companies_container.appendChild(card_container)
        company.market_values_list.forEach(market_value => {
            const market_value_tag = generateMarketValueTagElement(market_value)
            // Overwrite for remove the delete circle icon
            market_value_tag.innerHTML = market_value
            card.querySelector(".market-values-container").appendChild(market_value_tag)
        })

        card.querySelector(".delete-button").addEventListener("click", () => {
            api.companies.delete(company.id).then(response => {
                card_container.classList.add("d-none")
            })
        })

    })
} // end function

function main() {
    // Send button to create or save companies
    send_button = document.getElementById("send-button")
    send_button.addEventListener("click", handleCreateCompany)

    // Events for generate market value tags
    market_value_input = document.getElementById("market-value")
    market_value_input.addEventListener("keyup", handleCreateMarketValue)
    api.companies.list().then(response => generateCompaniesList(response))
} // end function

window.onload = main