import React from "react";

import ICPEditor from "../config/ICPEditor";
import PersonaEditor from "../config/PersonaEditor";
import TriggerEditor from "../config/TriggerEditor";

const Settings = () => {
  const icp = {
    industries: [
      "Artificial Intelligence",
      "SaaS"
    ],
    company_sizes: [
      "50-200",
      "200-1000"
    ],
    technologies: [
      "AWS",
      "OpenAI"
    ],
    regions: [
      "North America",
      "Europe"
    ]
  };

  const personas = [
    {
      id: "1",
      persona_name: "CTO",
      title:
        "Chief Technology Officer",
      department:
        "Technology"
    }
  ];

  const triggers = [
    {
      id: "1",
      trigger_name:
        "Funding Event",
      description:
        "Company recently raised funding.",
      enabled: true
    },
    {
      id: "2",
      trigger_name:
        "Hiring Surge",
      description:
        "Rapid hiring detected.",
      enabled: true
    }
  ];

  return (
    <div className="p-6 space-y-6">
      <h1 className="text-3xl font-bold">
        Platform Settings
      </h1>

      <ICPEditor
        initialConfig={icp}
        onSave={(data) =>
          console.log(data)
        }
      />

      <PersonaEditor
        personas={personas}
        onSave={(data) =>
          console.log(data)
        }
      />

      <TriggerEditor
        triggers={triggers}
        onSave={(data) =>
          console.log(data)
        }
      />
    </div>
  );
};

export default Settings;