
const API_KEY = ""
const submitIcon = document.querySelector("#submit-icon")
const inputElement = document.querySelector("input")
const imageSection = document.querySelector('.images-section')

const getImages = async () => {
    const options = {
        method : "POST", 
        headers: {
            "Authorization": 'Bearer ${API_KEY}', 
            "Content-Type": "applications/json"
        }, 

        body: JSON.stringify({
            prompt: inputElement.value, // Gets the input value of the user 
            n : 4, //Number of images that will be generated 
            size: "1024x1024" //Size of the images
        })
    }
    try {
        const response = await fetch("https://api.openai.com/v1/images/edits", options)  
        const data = await response.json()

        data?.data.array.forEach(imageObject => {
            const imageContainer = document.createElement("div")
            imageContainer.classList.add("image-container")
            const imageElement = document.createElement("img")
            imageElement.setAttribute("src", imageObject.url)
            imageContainer.append(imageElement)
            imageSection.append(imageContainer)
        });
    } catch (error) {
        console.error(error)
    }
}

submitIcon.addEventListener('click', getImages)