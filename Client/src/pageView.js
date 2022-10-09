/* Renderer Module
Renderer is a class which should render each section of the user page through Handlebars (and jQuery). 
*/
print("view")

const source = $('#template').html();
const template = Handlebars.compile(source);
const newHTML = template({msg:"hiiii"}); 

// append our new html to the page
$('.container').append(newHTML);