
import json
import requests

headers={
    "x-api-key":"x2YtaaayGv9lUXISFzRXU1TV3Ybzj04L6PzCoqNi",
    "Content-Type":"application/json"
}
payload={
    "data":"When Depositions May Be Taken. After commencement of the action, any party may take the testimony of any person, including a party, by deposition upon oral examination. Leave of court, granted with or without notice, must be obtained only if theWhen Depositions May Be Taken. After commencement of the action, any party may take the testimony of any person, including a party, by deposition upon oral examination. Leave of court, granted with or without notice, must be obtained only if the plaintiff seeks to take a deposition before the expiration of the period within which a defendant may file a responsive pleading under Rule 3:8, except that leave is not required (1) if a defendant has served a notice of taking deposition, or (2) if special notice is given as provided in subdivision (b)(2) of this Rule. The attendance of witnesses may be compelled by subpoena. The deposition of a person confined in prison may be taken only by leave of court on such terms as the court prescribes. (a1) Taking of Depositions (ii) Non-party Witness Depositions. Unless otherwise provided by the law of the jurisdictio where a non-party witness resides, a deposition of a non-party witness shall be taken in the county or city where the non-party witness resides, is employed, or has a principal place of business; at a place upon which the witness and the parties to the litigation agree; or at a place that the court may, for good cause, designate" \
    }

response=requests.post("https://23nt6yrife.execute-api.us-east-1.amazonaws.com/dev/ilabs-concept-extractor",data=json.dumps(payload),headers=headers)
print(json.dumps(response.json(),indent=4))