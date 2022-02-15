{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "f1d392e9",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "cd4e0ec4",
   "metadata": {},
   "outputs": [],
   "source": [
    "app=Flask(__name__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "2c662da3",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import request,render_template\n",
    "from keras.models import load_model\n",
    "@app.route(\"/\",methods=[\"GET\",\"POST\"])\n",
    "def index():\n",
    "    if request.method==\"POST\":\n",
    "        NPTA = request.form.get(\"NPTA\")\n",
    "        TLTA = request.form.get(\"TLTA\")\n",
    "        WCTA = request.form.get(\"WCTA\")\n",
    "        print(NPTA,TLTA,WCTA) \n",
    "        model=load_model(\"BKR\")\n",
    "        pred=model.predict([[float(NPTA),float(TLTA),float(WCTA)]])\n",
    "        print(pred)\n",
    "        s=\"The predicted bankruptcy score is:\"+str(pred)\n",
    "        return(render_template(\"index1.html\",result=s))\n",
    "    else:\n",
    "        return(render_template(\"index1.html\",result=\"2\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ed856730",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app \"__main__\" (lazy loading)\n",
      " * Environment: production\n",
      "\u001b[31m   WARNING: This is a development server. Do not use it in a production deployment.\u001b[0m\n",
      "\u001b[2m   Use a production WSGI server instead.\u001b[0m\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      " * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)\n",
      "127.0.0.1 - - [15/Feb/2022 10:58:58] \"GET / HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.1 0.1 0.1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [15/Feb/2022 10:59:05] \"POST / HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[0.59039176]]\n"
     ]
    }
   ],
   "source": [
    "if __name__==\"__main__\":\n",
    "    app.run()\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "08038493",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
