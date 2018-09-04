from __init__ import disable_avx2_warning
import tensorflow as tf

disable_avx2_warning()

foo = tf.constant('foo')
bar = tf.constant('bar')
foobar = foo + bar

with tf.Session() as session:
    answer = session.run(foobar)

print(answer)
