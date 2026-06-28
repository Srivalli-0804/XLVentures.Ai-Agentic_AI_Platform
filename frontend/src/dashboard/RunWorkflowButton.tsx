import React from "react";

interface Props {
  workflowName: string;
  onRun: (
    workflowName: string
  ) => Promise<void>;
}

const RunWorkflowButton: React.FC<Props> = ({
  workflowName,
  onRun
}) => {
  const handleClick = async () => {
    await onRun(workflowName);
  };

  return (
    <button
      onClick={handleClick}
      className="px-4 py-2 rounded-lg bg-blue-600 text-white hover:bg-blue-700"
    >
      Run Workflow
    </button>
  );
};

export default RunWorkflowButton;