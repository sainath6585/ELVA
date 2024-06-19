$(document).ready(function () {



    // Display Speak Message
    eel.expose(DisplayMessage)
    function doc_keyUp(e) {
        if (e.key === 'j') {
            eel.playAssistantSound();
            $("#Oval").attr("hidden", true);
            $("#SiriWave").attr("hidden", false);
            eel.allCommands()();
        }
    }
    

    // Display hood
    eel.expose(ShowHood)
    function ShowHood() {
        $("#Oval").attr("hidden", false);
        $("#Siriwave").attr("hidden", true);
    }

});