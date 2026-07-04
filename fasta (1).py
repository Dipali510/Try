{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "98631713-d075-4f05-b28b-fe82f6ff8d38",
   "metadata": {},
   "outputs": [],
   "source": [
    "def read_file(filename):\n",
    "    database={}\n",
    "    curr_id=None\n",
    "    curr_seq=\" \"\n",
    "    with open (filename,'r')as file:\n",
    "        curr_id=\" \"\n",
    "        for line in file:\n",
    "            line=line.strip()\n",
    "            if line.startswith(\">\"):\n",
    "                if curr_id:\n",
    "                    database[curr_id]=curr_seq\n",
    "                curr_id=line[1:]\n",
    "                curr_seq=\"\"\n",
    "            else:\n",
    "                curr_seq+=line\n",
    "    if curr_id:\n",
    "        database[curr_id]=curr_seq\n",
    "    return database\n",
    "            \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "88dc312f-44d7-49ad-8d7e-825e2781b9f0",
   "metadata": {},
   "outputs": [],
   "source": [
    "def score_pair(a,b):\n",
    "    if a==b:\n",
    "      return 4\n",
    "    elif(a==\"L\" and b==\"I\")or (a==\"I\" and b==\"L\"):\n",
    "      return 2\n",
    "    else:\n",
    "      return -1\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "7733c153-5bf4-4143-8813-281a8fe497e4",
   "metadata": {},
   "outputs": [],
   "source": [
    "def alig_scr(seq1,seq2):\n",
    "    score=0\n",
    "    for a,b in zip(seq1,seq2):\n",
    "        score+=score_pair(a,b)\n",
    "    return score"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "c56454a5-9b4c-497f-9709-3dd3a41e3737",
   "metadata": {},
   "outputs": [],
   "source": [
    "def percent(seq1,seq2):\n",
    "    match=0\n",
    "    for a,b in zip(seq1,seq2):\n",
    "         if a==b:\n",
    "           match+=1\n",
    "    return(match/len(seq1))*100"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "d5cbca84-bf39-4654-ae6f-64b35c7e43eb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter protein mlillm\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Protein: \n",
      "Sequence: \n",
      "alignment:-1\n",
      "identity:0.0\n",
      "Protein:Protein1\n",
      "Sequence:MILMMM\n",
      "alignment:10\n",
      "identity:33.33333333333333\n",
      "Protein:Protein2\n",
      "Sequence:MLILLM\n",
      "alignment:24\n",
      "identity:100.0\n",
      "best matchProtein2 with score24\n"
     ]
    }
   ],
   "source": [
    "database=read_file(\"protein.fasta\")\n",
    "query=input(\"enter protein\").upper()\n",
    "best_scr=float(\"-inf\")\n",
    "best_hit=\" \"\n",
    "best_seq=\" \"\n",
    "best_id=\" \"\n",
    "\n",
    "\n",
    "for protein_id,sequence in database.items():\n",
    "    score=alig_scr(query,sequence)\n",
    "    identity=percent(query,sequence)\n",
    "    print(f\"Protein:{protein_id}\")\n",
    "    print(f\"Sequence:{sequence}\")\n",
    "    print(f\"alignment:{score}\")\n",
    "    print(f\"identity:{identity}\")\n",
    "\n",
    "    \n",
    "    if score>best_scr:\n",
    "      best_scr=score\n",
    "      best_hit=protein_id\n",
    "      best_seq=sequence\n",
    "      best_id=identity\n",
    "        \n",
    "report = f\"best match{best_hit} with score{best_scr}\"\n",
    "print(report)\n",
    "\n",
    "\n",
    "\n",
    "                   "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "68ba18b3-8397-4f70-b707-5d7ef2e2a28d",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "149757d6-083c-4b24-9472-f1bcb6dd096b",
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
   "version": "3.14.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
