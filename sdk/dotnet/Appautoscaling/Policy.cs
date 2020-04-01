// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.AppAutoScaling
{
    /// <summary>
    /// Provides an Application AutoScaling Policy resource.
    /// 
    /// 
    /// ## Nested fields
    /// 
    /// ### `target_tracking_scaling_policy_configuration`
    /// 
    /// * `target_value` - (Required) The target value for the metric.
    /// * `disable_scale_in` - (Optional) Indicates whether scale in by the target tracking policy is disabled. If the value is true, scale in is disabled and the target tracking policy won't remove capacity from the scalable resource. Otherwise, scale in is enabled and the target tracking policy can remove capacity from the scalable resource. The default value is `false`.
    /// * `scale_in_cooldown` - (Optional) The amount of time, in seconds, after a scale in activity completes before another scale in activity can start.
    /// * `scale_out_cooldown` - (Optional) The amount of time, in seconds, after a scale out activity completes before another scale out activity can start.
    /// * `customized_metric_specification` - (Optional) A custom CloudWatch metric. Documentation can be found  at: [AWS Customized Metric Specification](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_CustomizedMetricSpecification.html). See supported fields below.
    /// * `predefined_metric_specification` - (Optional) A predefined metric. See supported fields below.
    /// 
    /// ### `customized_metric_specification`
    /// 
    /// * `dimensions` - (Optional) The dimensions of the metric.
    /// * `metric_name` - (Required) The name of the metric.
    /// * `namespace` - (Required) The namespace of the metric.
    /// * `statistic` - (Required) The statistic of the metric.
    /// * `unit` - (Optional) The unit of the metric.
    /// 
    /// ### `predefined_metric_specification`
    /// 
    /// * `predefined_metric_type` - (Required) The metric type.
    /// * `resource_label` - (Optional) Reserved for future use.
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/appautoscaling_policy.html.markdown.
    /// </summary>
    public partial class Policy : Pulumi.CustomResource
    {
        /// <summary>
        /// The ARN assigned by AWS to the scaling policy.
        /// </summary>
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        /// <summary>
        /// The name of the policy.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// For DynamoDB, only `TargetTrackingScaling` is supported. For Amazon ECS, Spot Fleet, and Amazon RDS, both `StepScaling` and `TargetTrackingScaling` are supported. For any other service, only `StepScaling` is supported. Defaults to `StepScaling`.
        /// </summary>
        [Output("policyType")]
        public Output<string?> PolicyType { get; private set; } = null!;

        /// <summary>
        /// The resource type and unique identifier string for the resource associated with the scaling policy. Documentation can be found in the `ResourceId` parameter at: [AWS Application Auto Scaling API Reference](http://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters)
        /// </summary>
        [Output("resourceId")]
        public Output<string> ResourceId { get; private set; } = null!;

        /// <summary>
        /// The scalable dimension of the scalable target. Documentation can be found in the `ScalableDimension` parameter at: [AWS Application Auto Scaling API Reference](http://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters)
        /// </summary>
        [Output("scalableDimension")]
        public Output<string> ScalableDimension { get; private set; } = null!;

        /// <summary>
        /// The AWS service namespace of the scalable target. Documentation can be found in the `ServiceNamespace` parameter at: [AWS Application Auto Scaling API Reference](http://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters)
        /// </summary>
        [Output("serviceNamespace")]
        public Output<string> ServiceNamespace { get; private set; } = null!;

        /// <summary>
        /// Step scaling policy configuration, requires `policy_type = "StepScaling"` (default). See supported fields below.
        /// </summary>
        [Output("stepScalingPolicyConfiguration")]
        public Output<Outputs.PolicyStepScalingPolicyConfiguration?> StepScalingPolicyConfiguration { get; private set; } = null!;

        /// <summary>
        /// A target tracking policy, requires `policy_type = "TargetTrackingScaling"`. See supported fields below.
        /// </summary>
        [Output("targetTrackingScalingPolicyConfiguration")]
        public Output<Outputs.PolicyTargetTrackingScalingPolicyConfiguration?> TargetTrackingScalingPolicyConfiguration { get; private set; } = null!;


        /// <summary>
        /// Create a Policy resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Policy(string name, PolicyArgs args, CustomResourceOptions? options = null)
            : base("aws:appautoscaling/policy:Policy", name, args ?? ResourceArgs.Empty, MakeResourceOptions(options, ""))
        {
        }

        private Policy(string name, Input<string> id, PolicyState? state = null, CustomResourceOptions? options = null)
            : base("aws:appautoscaling/policy:Policy", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Policy resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Policy Get(string name, Input<string> id, PolicyState? state = null, CustomResourceOptions? options = null)
        {
            return new Policy(name, id, state, options);
        }
    }

    public sealed class PolicyArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name of the policy.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// For DynamoDB, only `TargetTrackingScaling` is supported. For Amazon ECS, Spot Fleet, and Amazon RDS, both `StepScaling` and `TargetTrackingScaling` are supported. For any other service, only `StepScaling` is supported. Defaults to `StepScaling`.
        /// </summary>
        [Input("policyType")]
        public Input<string>? PolicyType { get; set; }

        /// <summary>
        /// The resource type and unique identifier string for the resource associated with the scaling policy. Documentation can be found in the `ResourceId` parameter at: [AWS Application Auto Scaling API Reference](http://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters)
        /// </summary>
        [Input("resourceId", required: true)]
        public Input<string> ResourceId { get; set; } = null!;

        /// <summary>
        /// The scalable dimension of the scalable target. Documentation can be found in the `ScalableDimension` parameter at: [AWS Application Auto Scaling API Reference](http://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters)
        /// </summary>
        [Input("scalableDimension", required: true)]
        public Input<string> ScalableDimension { get; set; } = null!;

        /// <summary>
        /// The AWS service namespace of the scalable target. Documentation can be found in the `ServiceNamespace` parameter at: [AWS Application Auto Scaling API Reference](http://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters)
        /// </summary>
        [Input("serviceNamespace", required: true)]
        public Input<string> ServiceNamespace { get; set; } = null!;

        /// <summary>
        /// Step scaling policy configuration, requires `policy_type = "StepScaling"` (default). See supported fields below.
        /// </summary>
        [Input("stepScalingPolicyConfiguration")]
        public Input<Inputs.PolicyStepScalingPolicyConfigurationArgs>? StepScalingPolicyConfiguration { get; set; }

        /// <summary>
        /// A target tracking policy, requires `policy_type = "TargetTrackingScaling"`. See supported fields below.
        /// </summary>
        [Input("targetTrackingScalingPolicyConfiguration")]
        public Input<Inputs.PolicyTargetTrackingScalingPolicyConfigurationArgs>? TargetTrackingScalingPolicyConfiguration { get; set; }

        public PolicyArgs()
        {
        }
    }

    public sealed class PolicyState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The ARN assigned by AWS to the scaling policy.
        /// </summary>
        [Input("arn")]
        public Input<string>? Arn { get; set; }

        /// <summary>
        /// The name of the policy.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// For DynamoDB, only `TargetTrackingScaling` is supported. For Amazon ECS, Spot Fleet, and Amazon RDS, both `StepScaling` and `TargetTrackingScaling` are supported. For any other service, only `StepScaling` is supported. Defaults to `StepScaling`.
        /// </summary>
        [Input("policyType")]
        public Input<string>? PolicyType { get; set; }

        /// <summary>
        /// The resource type and unique identifier string for the resource associated with the scaling policy. Documentation can be found in the `ResourceId` parameter at: [AWS Application Auto Scaling API Reference](http://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters)
        /// </summary>
        [Input("resourceId")]
        public Input<string>? ResourceId { get; set; }

        /// <summary>
        /// The scalable dimension of the scalable target. Documentation can be found in the `ScalableDimension` parameter at: [AWS Application Auto Scaling API Reference](http://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters)
        /// </summary>
        [Input("scalableDimension")]
        public Input<string>? ScalableDimension { get; set; }

        /// <summary>
        /// The AWS service namespace of the scalable target. Documentation can be found in the `ServiceNamespace` parameter at: [AWS Application Auto Scaling API Reference](http://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters)
        /// </summary>
        [Input("serviceNamespace")]
        public Input<string>? ServiceNamespace { get; set; }

        /// <summary>
        /// Step scaling policy configuration, requires `policy_type = "StepScaling"` (default). See supported fields below.
        /// </summary>
        [Input("stepScalingPolicyConfiguration")]
        public Input<Inputs.PolicyStepScalingPolicyConfigurationGetArgs>? StepScalingPolicyConfiguration { get; set; }

        /// <summary>
        /// A target tracking policy, requires `policy_type = "TargetTrackingScaling"`. See supported fields below.
        /// </summary>
        [Input("targetTrackingScalingPolicyConfiguration")]
        public Input<Inputs.PolicyTargetTrackingScalingPolicyConfigurationGetArgs>? TargetTrackingScalingPolicyConfiguration { get; set; }

        public PolicyState()
        {
        }
    }

    namespace Inputs
    {

    public sealed class PolicyStepScalingPolicyConfigurationArgs : Pulumi.ResourceArgs
    {
        [Input("adjustmentType")]
        public Input<string>? AdjustmentType { get; set; }

        [Input("cooldown")]
        public Input<int>? Cooldown { get; set; }

        [Input("metricAggregationType")]
        public Input<string>? MetricAggregationType { get; set; }

        [Input("minAdjustmentMagnitude")]
        public Input<int>? MinAdjustmentMagnitude { get; set; }

        [Input("stepAdjustments")]
        private InputList<PolicyStepScalingPolicyConfigurationStepAdjustmentsArgs>? _stepAdjustments;
        public InputList<PolicyStepScalingPolicyConfigurationStepAdjustmentsArgs> StepAdjustments
        {
            get => _stepAdjustments ?? (_stepAdjustments = new InputList<PolicyStepScalingPolicyConfigurationStepAdjustmentsArgs>());
            set => _stepAdjustments = value;
        }

        public PolicyStepScalingPolicyConfigurationArgs()
        {
        }
    }

    public sealed class PolicyStepScalingPolicyConfigurationGetArgs : Pulumi.ResourceArgs
    {
        [Input("adjustmentType")]
        public Input<string>? AdjustmentType { get; set; }

        [Input("cooldown")]
        public Input<int>? Cooldown { get; set; }

        [Input("metricAggregationType")]
        public Input<string>? MetricAggregationType { get; set; }

        [Input("minAdjustmentMagnitude")]
        public Input<int>? MinAdjustmentMagnitude { get; set; }

        [Input("stepAdjustments")]
        private InputList<PolicyStepScalingPolicyConfigurationStepAdjustmentsGetArgs>? _stepAdjustments;
        public InputList<PolicyStepScalingPolicyConfigurationStepAdjustmentsGetArgs> StepAdjustments
        {
            get => _stepAdjustments ?? (_stepAdjustments = new InputList<PolicyStepScalingPolicyConfigurationStepAdjustmentsGetArgs>());
            set => _stepAdjustments = value;
        }

        public PolicyStepScalingPolicyConfigurationGetArgs()
        {
        }
    }

    public sealed class PolicyStepScalingPolicyConfigurationStepAdjustmentsArgs : Pulumi.ResourceArgs
    {
        [Input("metricIntervalLowerBound")]
        public Input<string>? MetricIntervalLowerBound { get; set; }

        [Input("metricIntervalUpperBound")]
        public Input<string>? MetricIntervalUpperBound { get; set; }

        [Input("scalingAdjustment", required: true)]
        public Input<int> ScalingAdjustment { get; set; } = null!;

        public PolicyStepScalingPolicyConfigurationStepAdjustmentsArgs()
        {
        }
    }

    public sealed class PolicyStepScalingPolicyConfigurationStepAdjustmentsGetArgs : Pulumi.ResourceArgs
    {
        [Input("metricIntervalLowerBound")]
        public Input<string>? MetricIntervalLowerBound { get; set; }

        [Input("metricIntervalUpperBound")]
        public Input<string>? MetricIntervalUpperBound { get; set; }

        [Input("scalingAdjustment", required: true)]
        public Input<int> ScalingAdjustment { get; set; } = null!;

        public PolicyStepScalingPolicyConfigurationStepAdjustmentsGetArgs()
        {
        }
    }

    public sealed class PolicyTargetTrackingScalingPolicyConfigurationArgs : Pulumi.ResourceArgs
    {
        [Input("customizedMetricSpecification")]
        public Input<PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationArgs>? CustomizedMetricSpecification { get; set; }

        [Input("disableScaleIn")]
        public Input<bool>? DisableScaleIn { get; set; }

        [Input("predefinedMetricSpecification")]
        public Input<PolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecificationArgs>? PredefinedMetricSpecification { get; set; }

        [Input("scaleInCooldown")]
        public Input<int>? ScaleInCooldown { get; set; }

        [Input("scaleOutCooldown")]
        public Input<int>? ScaleOutCooldown { get; set; }

        [Input("targetValue", required: true)]
        public Input<double> TargetValue { get; set; } = null!;

        public PolicyTargetTrackingScalingPolicyConfigurationArgs()
        {
        }
    }

    public sealed class PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationArgs : Pulumi.ResourceArgs
    {
        [Input("dimensions")]
        private InputList<PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionsArgs>? _dimensions;
        public InputList<PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionsArgs> Dimensions
        {
            get => _dimensions ?? (_dimensions = new InputList<PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionsArgs>());
            set => _dimensions = value;
        }

        [Input("metricName", required: true)]
        public Input<string> MetricName { get; set; } = null!;

        [Input("namespace", required: true)]
        public Input<string> Namespace { get; set; } = null!;

        [Input("statistic", required: true)]
        public Input<string> Statistic { get; set; } = null!;

        [Input("unit")]
        public Input<string>? Unit { get; set; }

        public PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationArgs()
        {
        }
    }

    public sealed class PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionsArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name of the policy.
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        [Input("value", required: true)]
        public Input<string> Value { get; set; } = null!;

        public PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionsArgs()
        {
        }
    }

    public sealed class PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionsGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name of the policy.
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        [Input("value", required: true)]
        public Input<string> Value { get; set; } = null!;

        public PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionsGetArgs()
        {
        }
    }

    public sealed class PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationGetArgs : Pulumi.ResourceArgs
    {
        [Input("dimensions")]
        private InputList<PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionsGetArgs>? _dimensions;
        public InputList<PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionsGetArgs> Dimensions
        {
            get => _dimensions ?? (_dimensions = new InputList<PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionsGetArgs>());
            set => _dimensions = value;
        }

        [Input("metricName", required: true)]
        public Input<string> MetricName { get; set; } = null!;

        [Input("namespace", required: true)]
        public Input<string> Namespace { get; set; } = null!;

        [Input("statistic", required: true)]
        public Input<string> Statistic { get; set; } = null!;

        [Input("unit")]
        public Input<string>? Unit { get; set; }

        public PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationGetArgs()
        {
        }
    }

    public sealed class PolicyTargetTrackingScalingPolicyConfigurationGetArgs : Pulumi.ResourceArgs
    {
        [Input("customizedMetricSpecification")]
        public Input<PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationGetArgs>? CustomizedMetricSpecification { get; set; }

        [Input("disableScaleIn")]
        public Input<bool>? DisableScaleIn { get; set; }

        [Input("predefinedMetricSpecification")]
        public Input<PolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecificationGetArgs>? PredefinedMetricSpecification { get; set; }

        [Input("scaleInCooldown")]
        public Input<int>? ScaleInCooldown { get; set; }

        [Input("scaleOutCooldown")]
        public Input<int>? ScaleOutCooldown { get; set; }

        [Input("targetValue", required: true)]
        public Input<double> TargetValue { get; set; } = null!;

        public PolicyTargetTrackingScalingPolicyConfigurationGetArgs()
        {
        }
    }

    public sealed class PolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecificationArgs : Pulumi.ResourceArgs
    {
        [Input("predefinedMetricType", required: true)]
        public Input<string> PredefinedMetricType { get; set; } = null!;

        [Input("resourceLabel")]
        public Input<string>? ResourceLabel { get; set; }

        public PolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecificationArgs()
        {
        }
    }

    public sealed class PolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecificationGetArgs : Pulumi.ResourceArgs
    {
        [Input("predefinedMetricType", required: true)]
        public Input<string> PredefinedMetricType { get; set; } = null!;

        [Input("resourceLabel")]
        public Input<string>? ResourceLabel { get; set; }

        public PolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecificationGetArgs()
        {
        }
    }
    }

    namespace Outputs
    {

    [OutputType]
    public sealed class PolicyStepScalingPolicyConfiguration
    {
        public readonly string? AdjustmentType;
        public readonly int? Cooldown;
        public readonly string? MetricAggregationType;
        public readonly int? MinAdjustmentMagnitude;
        public readonly ImmutableArray<PolicyStepScalingPolicyConfigurationStepAdjustments> StepAdjustments;

        [OutputConstructor]
        private PolicyStepScalingPolicyConfiguration(
            string? adjustmentType,
            int? cooldown,
            string? metricAggregationType,
            int? minAdjustmentMagnitude,
            ImmutableArray<PolicyStepScalingPolicyConfigurationStepAdjustments> stepAdjustments)
        {
            AdjustmentType = adjustmentType;
            Cooldown = cooldown;
            MetricAggregationType = metricAggregationType;
            MinAdjustmentMagnitude = minAdjustmentMagnitude;
            StepAdjustments = stepAdjustments;
        }
    }

    [OutputType]
    public sealed class PolicyStepScalingPolicyConfigurationStepAdjustments
    {
        public readonly string? MetricIntervalLowerBound;
        public readonly string? MetricIntervalUpperBound;
        public readonly int ScalingAdjustment;

        [OutputConstructor]
        private PolicyStepScalingPolicyConfigurationStepAdjustments(
            string? metricIntervalLowerBound,
            string? metricIntervalUpperBound,
            int scalingAdjustment)
        {
            MetricIntervalLowerBound = metricIntervalLowerBound;
            MetricIntervalUpperBound = metricIntervalUpperBound;
            ScalingAdjustment = scalingAdjustment;
        }
    }

    [OutputType]
    public sealed class PolicyTargetTrackingScalingPolicyConfiguration
    {
        public readonly PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecification? CustomizedMetricSpecification;
        public readonly bool? DisableScaleIn;
        public readonly PolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecification? PredefinedMetricSpecification;
        public readonly int? ScaleInCooldown;
        public readonly int? ScaleOutCooldown;
        public readonly double TargetValue;

        [OutputConstructor]
        private PolicyTargetTrackingScalingPolicyConfiguration(
            PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecification? customizedMetricSpecification,
            bool? disableScaleIn,
            PolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecification? predefinedMetricSpecification,
            int? scaleInCooldown,
            int? scaleOutCooldown,
            double targetValue)
        {
            CustomizedMetricSpecification = customizedMetricSpecification;
            DisableScaleIn = disableScaleIn;
            PredefinedMetricSpecification = predefinedMetricSpecification;
            ScaleInCooldown = scaleInCooldown;
            ScaleOutCooldown = scaleOutCooldown;
            TargetValue = targetValue;
        }
    }

    [OutputType]
    public sealed class PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecification
    {
        public readonly ImmutableArray<PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensions> Dimensions;
        public readonly string MetricName;
        public readonly string Namespace;
        public readonly string Statistic;
        public readonly string? Unit;

        [OutputConstructor]
        private PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecification(
            ImmutableArray<PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensions> dimensions,
            string metricName,
            string @namespace,
            string statistic,
            string? unit)
        {
            Dimensions = dimensions;
            MetricName = metricName;
            Namespace = @namespace;
            Statistic = statistic;
            Unit = unit;
        }
    }

    [OutputType]
    public sealed class PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensions
    {
        /// <summary>
        /// The name of the policy.
        /// </summary>
        public readonly string Name;
        public readonly string Value;

        [OutputConstructor]
        private PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensions(
            string name,
            string value)
        {
            Name = name;
            Value = value;
        }
    }

    [OutputType]
    public sealed class PolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecification
    {
        public readonly string PredefinedMetricType;
        public readonly string? ResourceLabel;

        [OutputConstructor]
        private PolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecification(
            string predefinedMetricType,
            string? resourceLabel)
        {
            PredefinedMetricType = predefinedMetricType;
            ResourceLabel = resourceLabel;
        }
    }
    }
}
