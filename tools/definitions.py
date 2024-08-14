"""
    This file contains json-schemas for the tools

"""

GET_WEATHER_INFORMATION = {
    "type": "function",
    "function": {
        "name": "get_weather_information",
        "description": "Gets the weather information for a given latitude and longitude",
        "parameters": {
            "type": "object",
            "properties": {
                "latitude": {
                    "type": "number",
                    "description": "The latitude of the location",
                },
                "longitude": {
                    "type": "number",
                    "description": "The longitude of the location",
                },
            },
            "required": ["latitude", "longitude"],
        },
    },
}



tool_item ={ 
      "type": "function",
      "function": {
            "name": "update_user_information",
            "description": "insert or update user's infomations. name, age, gender, medical history",
            "parameters": {
            "type": "object",
            "properties": {
                "name": {
                    "description": "User's full name",
                    "type": "string"
                },
                "age": {
                    "description": "User's age",
                    "type": "number"
                },
                "birthdate": {
                    "description": "User's birth date( MM/DD )",
                    "type": "string"
                },
                "gender": {
                    "description": "User's gender)",
                    "unit": [
                    "male",
                    "female",
                    "non-binary"
                    ],
                    "type": "string"
                }
            },
            "required": []
        }
    }
}
tool_item2 = {
    "type": "function",
    "function": {
        "name": "record_user_activity",
        # "description": "대화 상대의 활동내역을 저장한다. 방문한 장소, 운동내역, 식사내역, 쉬는 활동 , 업무 , 자원봉사등 가능한 모든 활동 내역을 저장한다.",
        "description": "会話相手の活動履歴を保存する。訪れた場所、運動記録、食事記録、休憩活動、仕事、ボランティアなど、可能な限りすべての活動履歴を保存する。",
        "parameters": {
            "type": "object",
            "properties": {
            "type": {
                # "description": "사용자 활동의 유형",
                "description": "ユーザー活動の種類",
                "unit": [
                "work out",
                "leisure",
                "work",
                "Volunteer",
                "social activity",
                "meal",
                "shopping",
                "etc"
                ],
                "type": "string"
            },
            "desc": {
                # "description": "User activity에 대한 내용. 어떤 활동을 했는지 설명",
                "description": "ユーザー活動の内容。どのような活動をしたかを説明",
                "type": "string"
            }

            },
            "required": ['type','desc']
        }
    }
}

tool_item4 = {
    "type": "function",
    "function": {
        "name": "record_schedule",
        # "description": "대화 상대의 일정을 저장한다. 현재 이후의 일정이 파악되면 그 내용을 저장한다.",
        "description": "会話相手のスケジュールを保存する。現在以降のスケジュールが把握できればその内容を保存する。",
        "parameters": {
            "type": "object",
            "properties": {
            "type": {
                # "description": "일정의 유형",
                "description": "スケジュールの種類",
                "unit": [
                "work out",
                "leisure",
                "work",
                "Volunteer",
                "social activity",
                "meal",
                "shopping",
                "hospital appointment"
                "etc"
                ],
                "type": "string"
            },
            "desc": {
                # "description": "일정의 내용",
                "description": "スケジュールの内容",
                "type": "string"
            },
            "date": {
                # "description": "일정의 일자 YYYY-MM-DD",
                "description": "スケジュールの日付 YYYY-MM-DD",
                "type": "string"
            },
            "time": {
                # "description": "일정의 시간 HH:mm:ss",
                "description": "スケジュールの時間 HH:mm:ss",
                "type": "string"
            }

            },
            "required": ['type','desc','date']
        }
    }
}

tool_item3 = {
    "type": "function",
    "function": {
        "name": "insert_user_medical_history",
        # "description": "대화 상대의 의료 기록을 저장한다. 가지고 있는 병력이나 건강 상태에 대한 정보를 저장한다.",
        "description": "会話相手の医療記録を保存する。持っている病歴や健康状態に関する情報を保存する。",
        "parameters": {
            "type": "object",
            "properties": {
                "disease_name": {
                    "description": "병명. 병의 내용을 기록한다",
                    "description": "病名。病気の内容を記録する",
                    "type": "string"
                },
                "desc": {
                # "description": "병과 관련된 상세 사항. 입원, 치료 내용, 치료 결과등 병과 관련된 추가 정보를 저장",
                "description": "病気に関連する詳細事項。入院、治療内容、治療結果など、病気に関連する追加情報を保存",
                "type": "string"
                }      
            },
            "required": ['disease_name']
        }
    }
}

LIFELIFT_TOOLS = [
    tool_item, tool_item2 , tool_item3, tool_item4
]
