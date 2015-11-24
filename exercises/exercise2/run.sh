python getQuestions.py Posts.xml
python getAnswers.py Posts.xml
python getTag.py Posts.xml algorithms
python doJoin.py algorithms.txt questions.txt 1 1 algorithms-posts.txt
python doJoin.py answers.txt algorithms-posts.txt 1 3 qa.txt
python getStats.py qa.txt 2 6  >> result.txt