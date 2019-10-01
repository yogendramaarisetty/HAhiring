var lang = "Java"
var e = ace.edit("code")
e.getSession().setMode("ace/mode/java");
e.setFontSize("15px");
e.setValue("//Write your Java Code below\n\nimport java.util.*;\npublic class Main{\n\tpublic static void main(String args[]){\n\tScanner scan = new Scanner(System.in);\n\tSystem.out.println();\n\t}\n}");
$(document).ready(function() {
    $('.loader').hide();
    $('#tctable').hide();
});


function selectLang() {
    lang = document.getElementById("language").value;

    if (lang == "Java") {
        e.getSession().setMode("ace/mode/java");
        e.setFontSize("15px");
        e.setValue("//Write your Java Code below\n\n import java.util.*;\npublic class Main{\n\tpublic static void main(String args[]){\n\tScanner scan = new Scanner(System.in);\n\tSystem.out.println();\n\t}\n}");

    }
    if (lang == "C") {
        e.getSession().setMode("ace/mode/c_cpp");
        e.setFontSize("15px");
        e.setValue("//Write your C code Below\n\n #include <stdio.h>\n\nint main(){\n printf();\n}");
    }
    if (lang == "C++") {
        e.getSession().setMode("ace/mode/c_cpp");
        e.setFontSize("15px");
        e.setValue("//Write your C++ code below\n\n#include<iostream>\n using namespace std;\n int main(){\ncout<<;\n}");
    }
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
                    $('#tc1').css("color", "white")
                    $('#tc1').css("background-color", "green")
                } else {
                    $('#tc1').css("color", "white")
                    $('#tc1').css("background-color", "red")

                }
                if ($('#tc2').text() == "Passed") {
                    $('#tc2').css("color", "white")
                    $('#tc2').css("background-color", "green")
                } else {
                    $('#tc2').css("color", "white")
                    $('#tc2').css("background-color", "red")

                }
                if ($('#tc3').text() == "Passed") {
                    $('#tc3').css("color", "white")
                    $('#tc3').css("background-color", "green")
                } else {
                    $('#tc3').css("color", "white")
                    $('#tc3').css("background-color", "red")

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