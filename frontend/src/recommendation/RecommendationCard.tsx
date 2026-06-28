import React from "react";

export interface Recommendation {
  id: string;
  company_name: string;
  contact_name: string;
  recommendation_type: string;
  priority: string;
  message: string;
}

interface Props {
  recommendation: Recommendation;
}

const priorityColor = (
  priority: string
) => {
  switch (priority.toLowerCase()) {
    case "high":
      return "bg-red-100 text-red-700";

    case "medium":
      return "bg-yellow-100 text-yellow-700";

    default:
      return "bg-green-100 text-green-700";
  }
};

const RecommendationCard: React.FC<Props> = ({
  recommendation
}) => {
  return (
    <div className="bg-white shadow rounded-lg p-5 border">
      <div className="flex justify-between items-center">
        <h3 className="font-semibold text-lg">
          {recommendation.company_name}
        </h3>

        <span
          className={`px-3 py-1 rounded-full text-sm ${priorityColor(
            recommendation.priority
          )}`}
        >
          {recommendation.priority}
        </span>
      </div>

      <div className="mt-2 text-gray-700">
        Contact:{" "}
        {recommendation.contact_name}
      </div>

      <div className="mt-2">
        <span className="font-medium">
          Type:
        </span>{" "}
        {
          recommendation.recommendation_type
        }
      </div>

      <div className="mt-4 bg-gray-50 rounded p-3">
        {recommendation.message}
      </div>
    </div>
  );
};

export default RecommendationCard;