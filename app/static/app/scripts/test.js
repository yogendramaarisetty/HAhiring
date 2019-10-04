var lang = "Java"
var e = ace.edit("code")
e.getSession().setMode("ace/mode/java");
e.setFontSize("15px");

function java_default() {
    e.setValue("//Write your Java Code below\n//NOTE:Public Class Must be Main\n\nimport java.util.*;\npublic class Main{\n\tpublic static void main(String args[]){\n\tScanner scan = new Scanner(System.in);\n\tSystem.out.println();\n\t}\n}");
}
$(document).ready(function() {
    java_default();
    $('.loader').hide();
    $('#tctable').hide();
    $('#submit_warn').hide();


});

if ($("#myTimer").text() == "00:00") {
    submitCode();

}
if ($("#myTimer").text() == "59:55") {
    alert("timer logged");
    submitCode();

}





function runCode() {


    if (e.getValue() != "") {
        $('.loader').show();
        var ajaxMins = new Date().getMinutes();
        var ajaxSecs = new Date().getSeconds();
        var ajaxMS = new Date().getMilliseconds();
        $.ajax({
            type: 'POST',
            url: 'code1/',
            dataType: 'json',
            cache: false,
            async: true,
            data: {
                csrfmiddlewaretoken: '{{ csrf_token }}',
                code: e.getValue(),
                input: $('#input').val(),
                language_id: lang,

            },
            success: function(json) {
                $('.loader').hide();
                $('#output').html(json.msg);


            }

        }).done(function() {
            var ajaxMins2 = new Date().getMinutes() - ajaxMins;
            var ajaxSecs2 = (new Date().getSeconds() % 60) - ajaxSecs;
            var ajaxMS2 = new Date().getMilliseconds() - ajaxMS;

            console.log(ajaxSecs2, " seconds");
        });
    } else {
        $('#output').html("Don't submit empty code");
    }
}

function submitCode() {

    e.setValue(e.getValue());
    if (e.getValue() != "") {

        $('.loader').show();
        var ajaxMins = new Date().getMinutes();
        var ajaxSecs = new Date().getSeconds();
        var ajaxMS = new Date().getMilliseconds();
        $.ajax({
            type: 'POST',
            url: 'code1/',
            dataType: 'json',
            cache: false,
            async: true,
            data: {
                csrfmiddlewaretoken: '{{ csrf_token }}',
                code: e.getValue(),
                input: $('#input').val(),
                submit: "yes",
            },
            success: function(json) {
                $('.loader').hide();
                $('#tctable').show();
                var pass = "<p color>Passed<p>";
                var fail = "<p>Failed <p>";
                $('#tc1').html(json.testcase1 == true ? pass : fail);
                $('#tc2').html(json.testcase2 == true ? pass : fail);
                $('#tc3').html(json.testcase3 == true ? pass : fail);
                $('#tc4').html(json.testcase4 == true ? pass : fail);

                if ($('#tc1').text() == "Passed") {
                    $('#tc1').css("color", "green")
                    $('#tc1').css("background-color", "white")
                } else {
                    $('#tc1').css("color", "red")
                    $('#tc1').css("background-color", "white")

                }
                if ($('#tc2').text() == "Passed") {
                    $('#tc2').css("color", "white")
                    $('#tc2').css("background-color", "green")
                } else {
                    $('#tc2').css("color", "white")
                    $('#tc2').css("background-color", "red")

                }
                if ($('#tc3').text() == "Passed") {
                    $('#tc3').css("color", "white");
                    $('#tc3').css("background-color", "green");
                } else {
                    $('#tc3').css("color", "Red");
                    $('#tc3').css("font-size", "20px")

                }
                if ($('#tc4').text() == "Passed") {
                    $('#tc4').css("color", "white")
                    $('#tc4').css("background-color", "green")
                } else {
                    $('#tc4').css("color", "white")
                    $('#tc4').css("background-color", "red")

                }





            }

        }).done(function() {
            var ajaxMins2 = new Date().getMinutes() - ajaxMins;
            var ajaxSecs2 = (new Date().getSeconds() % 60) - ajaxSecs;
            var ajaxMS2 = new Date().getMilliseconds() - ajaxMS;

            console.log(ajaxSecs2, " seconds");
        });
    } else {
        $('#output').html("Don't submit empty code");
    }
}

document.addEventListener('DOMContentLoaded', function() {
    var checkbox = document.querySelector('input[type="checkbox"]');

    checkbox.addEventListener('change', function() {
        if (checkbox.checked) {
            e.setTheme("ace/theme/monokai")
            console.log('Checked');
        } else {
            // do that
            e.setTheme("ace/theme/xcode")
            console.log('Not checked');
        }
    });
});
var code = ace.edit("code", {
    theme: "ace/theme/chaos"
})

function update() {
    var shouldShow = !code.session.getValue().length;
    var node = code.renderer.emptyMessageNode;
    if (!shouldShow && node) {
        code.renderer.scroller.removeChild(code.renderer.emptyMessageNode);
        code.renderer.emptyMessageNode = null;
    } else if (shouldShow && !node) {
        node = code.renderer.emptyMessageNode = document.createElement("div");
        node.textContent = "Write you java code here"
        node.className = "ace_emptyMessage"
        node.style.padding = "0 9px"
        node.style.position = "absolute"
        node.style.zIndex = 9
        node.style.opacity = 0.5
        code.renderer.scroller.appendChild(node);
    }
}

code.on("input", update);
setTimeout(update, 100);

function startTimer(duration, display) {


    var start = Date.now(),
        diff,
        minutes,
        seconds;

    function timer() {
        // get the number of seconds that have elapsed since
        // startTimer() was called
        diff = duration - (((Date.now() - start) / 1000) | 0);

        // does the same job as parseInt truncates the float
        minutes = (diff / 60) | 0;
        seconds = (diff % 60) | 0;

        minutes = minutes < 10 ? "0" + minutes : minutes;
        seconds = seconds < 10 ? "0" + seconds : seconds;

        display.textContent = minutes + ":" + seconds;

        if (diff <= 0) {
            // add one second so that the count down starts at the full duration
            // example 05:00 not 04:59
            start = Date.now() + 1000;
        }
    };
    // we don't want to wait a full second before the timer starts
    timer();
    setInterval(timer, 1000);
}

window.onload = function() {
    var givenTime = document.getElementById("myTimer").innerHTML;
    givenTime = givenTime.split(":");
    var mins = Number(givenTime[0]);
    var secs = Number(givenTime[1]);

    var fiveMinutes = (60 * mins) + secs,
        display = document.querySelector('#myTimer');
    startTimer(fiveMinutes, display);
};

// Set the date we're counting down to
window.onload = function() {
    var dt = new Date();
    dt.setMinutes(dt.getMinutes() + 60);


    var countDownDate = new Date(dt).getTime();

    // Update the count down every 1 second
    var x = setInterval(function() {

        // Get today's date and time
        var now = new Date().getTime();


        // Find the distance between now and the count down date
        var distance = countDownDate - now;

        // Time calculations for days, hours, minutes and seconds
        var days = Math.floor(distance / (1000 * 60 * 60 * 24));
        var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        var seconds = Math.floor((distance % (1000 * 60)) / 1000);

        // Output the result in an element with id="demo"
        document.getElementById("myTimer1").innerHTML = +minutes + " : " + seconds + " ";
        if (minutes == 0) {
            if (seconds == 15) {
                document.getElementById("myTimer1").innerHTML = +minutes + " TIMEUP: " + seconds + " ";
                submitCode();


            }
        }
        if (minutes == 0) {
            if (seconds == 0) {

                document.getElementById('submitTest').click();
            }
        }
        // If the count down is over, write some text 
        if (distance < 0) {
            clearInterval(x);
            document.getElementById("myTimer1").innerHTML = "EXPIRED";
            document.getElementById('submitTest').click();
        }
    }, 1000);
}