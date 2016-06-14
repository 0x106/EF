

from subprocess import call

file = open("/Users/jordancampbell/Desktop/EF/output_file.txt", "w")

results = call(["googler", " bonsai ", ">| "], stdout=file)