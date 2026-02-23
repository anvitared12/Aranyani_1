# API endpoints of Aranyani App 
## Authentication APIs

| Method | Endpoint         | Role   | Description           | Request Body          | Response              |
| ------ | ---------------- | ------ | --------------------- | --------------------- | --------------------- |
| POST   | `/auth/register` | Public | Register new user     | name, email, password | JWT token + user info |
| POST   | `/auth/login`    | Public | User login            | email, password       | JWT token + role      |
| GET    | `/auth/me`       | User   | Get logged-in profile | —                     | User profile data     |

##  Plant Identification and Disease detection APIs
| Method | Endpoint                  | Role | Description                  | Request Body | Response                  |
| ------ | ------------------------- | ---- | ---------------------------- | ------------ | ------------------------- |
| POST   | `/plant/identify`         | User | Scan image to identify plant | image file   | Plant name + confidence   |
| POST   | `/plant/detect-disease`   | User | Scan plant to detect disease | image file   | Disease name + severity   |
| GET    | `/plant/details/:plantId` | User | Get detailed plant info      | —            | Growing guide + care info |

## Garden Scaning APIs
| Method | Endpoint            | Role | Description                   | Request Body                  | Response                     |
| ------ | ------------------- | ---- | ----------------------------- | ----------------------------- | ---------------------------- |
| POST   | `/garden/scan-area` | User | Scan growing area             | image/video                   | Light direction + space info |
| POST   | `/garden/recommend` | User | Recommend crops               | pot size, direction, location | List of suitable plants      |
| POST   | `/garden/add`       | User | Add plant to personal library | plantId                       | Success message              |

## Disease Solution APIs
| Method | Endpoint            | Role | Description             | Request Body         | Response        |
| ------ | ------------------- | ---- | ----------------------- | -------------------- | --------------- |
| POST   | `/disease/solution` | User | Get treatment solution  | diseaseId            | Treatment steps |

## Personal Plant Library APIs
| Method | Endpoint                   | Role | Description            | Request Body | Response             |
| ------ | -------------------------- | ---- | ---------------------- | ------------ | -------------------- |
| GET    | `/library`                 | User | Get user plant library | —            | List of saved plants |
| POST   | `/library/add`             | User | Add plant to library   | plantId      | Success              |
| DELETE | `/library/remove/:plantId` | User | Remove plant           | —            | Success              |

## Reminder APIs
| Method | Endpoint              | Role | Description              | Request Body       | Response           |
| ------ | --------------------- | ---- | ------------------------ | ------------------ | ------------------ |
| POST   | `/reminder/water`     | User | Set watering reminder    | plantId, frequency | Reminder scheduled |
| POST   | `/reminder/fertilize` | User | Set fertilizing reminder | plantId, frequency | Reminder scheduled |
| GET    | `/reminder`           | User | Get reminders            | —                  | List of reminders  |

## ML / AI APIs (Internal Layer)
| Method | Endpoint                     | Role     | Description        | Request Body     | Response          |
| ------ | ---------------------------- | -------- | ------------------ | ---------------- | ----------------- |
| POST   | `/ml/plant-classification`   | Internal | Predict plant type | image tensor     | Plant label       |
| POST   | `/ml/disease-classification` | Internal | Predict disease    | image tensor     | Disease label     |
| POST   | `/ml/recommendation-engine`  | Internal | Recommend crops    | environment JSON | Ranked plant list |
