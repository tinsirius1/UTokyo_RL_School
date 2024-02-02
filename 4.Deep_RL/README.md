# If you want to run on Colab
If you want to use this notebook on google Colab, put this cell on the top and run it first
```
! git clone https://github.com/tinsirius/Week08 >> /dev/null 2>&1
! apt install swig >> /dev/null 2>&1 
! pip install gym==0.26.0 otter-grader==3.3.0 pygame Box2D swig >> /dev/null 2>&1 
! pip install box2d-kengz >> /dev/null 2>&1 
```

Then move the Support folder for Week08 out accordingly. 

# Note on doing exercise in Colab: 

- I have no full authority over the environment on Colab, so the randomness is impossible to control, 
note that `LunarLander-v2` is a probabilistic environment so not every run is going to be the same! That 
means for the Exercise, if you use Colab, after training with Exercise notebook you have to copy your
`.pt` file to either Deepnote, Binder or local Docker to see what will your average return look like 
on my end! For example you might get average return of 201.24 on Colab but you might get average return 
of 199.08 when I grade, losing you 1 mark! So if you want to make absolute sure, please try your `.pt`
on Deepnote, Binder or local Docker

- Colab only allows 1 notebook as the "running" notebook at one time, so if you want to check `otter`, you
have to run the exercise first, download your `.pt`, open Colab again with `DeepRL_Exercise_Grading.ipynb`,
upload the `.pt`, and run `DeepRL_Exercise_Grading.ipynb` (with the Colab practice above, with the `git clone`
and moving and everything).
