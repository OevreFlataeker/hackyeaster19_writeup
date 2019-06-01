#import pytesseract
import re
import sys
import argparse
'''try:
    import Image
except ImportError:
    from PIL import Image
from subprocess import check_output


def resolve(path):
	print("Resampling the Image")
	#check_output(['convert', path, '-resample', '600', path])
	return pytesseract.image_to_string(Image.open(path))
'''
'''
captcha_text = resolve("captcha1.png")
print('Extracted Text',captcha_text)
if __name__=="__main__":
	argparser = argparse.ArgumentParser()
	argparser.add_argument('path',help = 'Captcha file path')
	args = argparser.parse_args()
	path = args.path
	print('Resolving Captcha')
	captcha_text = resolve(path)
	print('Extracted Text',captcha_text)
'''


webpage = '''<!DOCTYPE html>
<html lang="en">

<head>
    <title>Travel Navigator</title>
    <link rel="stylesheet" href="/static/css/fa-5.6.3.min.css">
    <link rel="stylesheet" href="/static/css/bootstrap.min.css">
    <link rel="stylesheet" href="/static/css/main.css">
</head>


<body>
<script src="/static/js/jquery-3.3.1.min.js"></script>

<!-- Navigation -->
<nav class="navbar navbar-expand-lg navbar-dark bg-dark static-top">
    <div class="container">
        <a class="navbar-brand" href="/"><i class="fas fa-drafting-compass"></i> Travel
            Navigator</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarResponsive"
                aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarResponsive">
            <ul class="navbar-nav ml-auto">

                    <li class="nav-item">
                        <a class="nav-link" href="/exit">
                            <button class="btn btn-danger">Exit</button>
                        </a>
                    </li>

            </ul>
        </div>
    </div>
</nav>

<!-- Page Content -->
<div class="container">
    <div class="row">
        <div class="col-lg-12">
            <h1 class="mt-5"></h1>





    <div class="row">
        <div class="col-3" style="border-right: 1px solid black">
            <span class="font-weight-bold">Carrots</span>
            <br>

                🥕


                🥕


                🥕


                🥕


                🥕

                    <br>


                🥕


                🥕


                🥕


                🥕


                🥕


            <hr>
            <div style="height: 200px">
                <h5>Navigator says:</h5>
                <p>[TURNED OFF]</p>

            </div>


                <hr>
                <h6>Solved:</h6>
                <div>
                    <ul class="checkmark">

                            <li class="tick">Warmup</li>

                    </ul>
                </div>

        </div>
        <div class="col-9">

    <h3><span style="color:red">WARNING!</span><br>
        C0tt0nt4il Ch3ck V2.0 required</h3>
    <img src="/static/img/ch12.jpg">
    <hr>


        <p>You need 10 right answers in time!</p>

        <img id="captcha" src="static/img/ch12/challenges/b9d6f93f-6a01-118-9b1d-0ffd07125efe.png">
        <div class="py-3">
            <form class="d-inline-block">
                <input class="form-control mb-3" type="text" name="result" autofocus>
                <input type="submit" class="btn btn-primary" value="I got it!">
            </form>
        </div>
        <code>0 correct answers.</code>



        </div>
    </div>


        </div>
    </div>
</div>

<!-- Bootstrap core JavaScript -->

<script type="application/javascript" src="/static/js/popper.min.js"></script>
<script type="application/javascript" src="/static/js/bootstrap.min.js"></script>

<script>
    $(function () {
        $('[data-toggle="popover"]').popover()
    })
</script>
</body>

</html>
'''

regex = '<img id="captcha" src="static/img/ch12/challenges/[0-9a-f]{8}-[0-9a-z]{4}-(.*)-[0-9a-z]{4}-[0-9a-z]{12}.png"'
hit = re.findall(regex, webpage)
print(hit)

