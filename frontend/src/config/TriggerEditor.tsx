import React, { useState } from "react";

interface TriggerRule {
  id: string;
  trigger_name: string;
  description: string;
  enabled: boolean;
}

interface Props {
  triggers: TriggerRule[];
  onSave: (
    triggers: TriggerRule[]
  ) => void;
}

const TriggerEditor: React.FC<Props> = ({
  triggers,
  onSave
}) => {
  const [data, setData] =
    useState(triggers);

  const toggleTrigger = (
    index: number
  ) => {
    const copy = [...data];

    copy[index].enabled =
      !copy[index].enabled;

    setData(copy);
  };

  return (
    <div className="bg-white rounded-lg shadow p-5">
      <h2 className="text-xl font-bold mb-4">
        Trigger Rules
      </h2>

      {data.map((trigger, index) => (
        <div
          key={trigger.id}
          className="flex justify-between items-center border p-3 rounded mb-2"
        >
          <div>
            <div className="font-semibold">
              {trigger.trigger_name}
            </div>

            <div className="text-sm text-gray-500">
              {trigger.description}
            </div>
          </div>

          <input
            type="checkbox"
            checked={trigger.enabled}
            onChange={() =>
              toggleTrigger(index)
            }
          />
        </div>
      ))}

      <button
        onClick={() => onSave(data)}
        className="bg-blue-600 text-white px-4 py-2 rounded mt-3"
      >
        Save Triggers
      </button>
    </div>
  );
};

export default TriggerEditor;