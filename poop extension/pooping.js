chrome.runtime.onInstalled.addListener(function() {
	chrome.storage.sync.set({color: "#ffb6c1"}, function(){console.log("The colour is punk");});
});