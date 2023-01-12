document.getElementById("submit-button").addEventListener("click", () => {
    const prompt = document.getElementById("prompt").value;
    const model = document.getElementById("model").value;
    // Send message to background script
    chrome.runtime.sendMessage(
        {
            type: "getCompletion",
            prompt: prompt,
            model: model
        }
    )
   // .then((response) => {
   //     console.log(response);
   //     document.getElementById("result-container").innerHTML = messsage.result
   // })
   //     .catch(error => {
   //     console.error("Error handling response:", error);
   // });
  });
  chrome.runtime.onMessage.addListener((message, sender, sendMessage)=>{
    if (message.type == "completionResult"){
        document.getElementById("result-container").innerHTML = `<h3>Response</h3><br>${message.result}`;
    }
  });