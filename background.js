//communicates between the extension and flask
chrome.runtime.onMessage.addListener(async (request, sender, sendResponse) => {
    // Handle message from extension
    console.log(request);
    if (request.type === "getCompletion") {
      // Send request to Flask application
      const response = await fetch("http://127.0.0.1:5000/completion", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          prompt: request.prompt,
          model: request.model
        }),
        mode: "cors"
      });
      const data = await response.json();
      console.log(data);

      // Check if the response is an error
      if (response.status !== 200) {
        // Throw an error which will be caught by the try/catch block in content.js
        throw new Error(response.statusText);
      }
  
      // Send response back to extension
      sendResponse({
        type: "completionResult",
        result: data.result
      });

      chrome.runtime.sendMessage(
        {
            type: "completionResult",
            result: data.result
        }
    );
    };
  });
  