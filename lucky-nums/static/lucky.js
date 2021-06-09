/** processForm: get data from form and make AJAX call to our API. */

async function processForm(evt) {
    evt.preventDefault()
    const name = $('#name').val()
    const email = $('#email').val()
    const year = $('#year').val()
    const color = $('#color').val()
    const response = await axios.post('/api/get-lucky-num', {name:name, email:email, year:year, color:color})
    handleResponse(response.data)
}

/** handleResponse: deal with response from our lucky-num API. */

function handleResponse(resp) {
   console.log(resp)
   $('#lucky-results').html(``)
   
    $('#lucky-results').html(`<p><h1>Your birth year ${resp.year}. The fact is ${resp.year_fact}</h1></p>
    <p><h1>Your lucky number is ${resp.num}. The fact is ${resp.num_fact}</h1></p>`)
}


$("#lucky-form").on("submit", processForm);
